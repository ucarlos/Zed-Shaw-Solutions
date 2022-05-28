from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)


@app.route("/")
def index():
    # This is used to 'setup' the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for('game'))


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    container = planisphere.RoomContainer()
    if request.method == "GET":
        if room_name:
            room = container.load_room(room_name)
            return render_template('show_room.html', room=room)
        else:
            # why is there here? Do you need it?
            return render_template('you_died.html')
    else:
        action = request.form.get('action')
        action = action.lower()
        if room_name and action:
            room = container.load_room(room_name)

            # Disable help if already enabled:
            room.disable_help()
            next_room = room.go(action)
            if not next_room:
                if action == "help":
                    room.enable_help()
                elif room.max_chances != -1:
                    room.current_chances -= 1
                    if not room.current_chances:
                        # Use * as the path for game over for chances:
                        room.current_chances = room.max_chances
                        session['room_name'] = container.name_room(room.go('*'))
                else:
                    session['room_name'] = container.name_room(room)
            else:
                session['room_name'] = container.name_room(next_room)

            # Check if session is None:
            if session['room_name'] is None:
                return render_template("Invalid_Input.html")
            return redirect(url_for('game'))


# YOU SHOULD CHANGE THIS IF YOU PLACE THIS APP ON THE INTERNET:
app.secret_key = 'b388bb04e37ec80012dfe77d3ff1aff39ab5f37ba265b5d2'

if __name__ == '__main__':
    app.run()
