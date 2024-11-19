from flask import Flask, request, jsonify
import pandas as pd

print(pd.__version__)

app = Flask(__name__)

practice_sets_file = "practice_sets.csv"
user_history_file = "data/user_history.csv"

practice_sets = pd.read_csv(practice_sets_file)
user_history = pd.read_csv(user_history_file)

def get_next_set(username, level):
    
    global user_history

    if username not in user_history['username'].unique():
        print(f"Adding new user: {username}")
        user_history = pd.concat([user_history, pd.DataFrame([{
            "username": username,
            "set_id": None,
            "times_completed": 0
        }])], ignore_index=True)
        user_history.to_csv(user_history_file, index=False)

    eligible_sets = practice_sets[practice_sets['level']==level]
    
    user_data = user_history[user_history['username'] == username]
    completed_counts = user_data.groupby('set_id')['times_completed'].sum().to_dict()

    eligible_sets['completion_count'] = eligible_sets['id'].map(completed_counts).fillna(0)
    next_set = eligible_sets.sort_values(by='completion_count').iloc[0]
    return next_set.to_dict()

@app.route('/get_practice_set', methods=['POST'])
def get_practice_set():
    data = request.json
    username = data.get('username')
    level = data.get('level')

    if not username or not level:
        return jsonify({"error": "Invalid input"}), 400

    try:
        next_set = get_next_set(username, level)
        return jsonify(next_set), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/update_history', methods=['POST'])
def update_history():
    data = request.json
    username = data.get('username')
    set_id = data.get('set_id')

    if not username or not set_id:
        return jsonify({"error": "Invalid input"}), 400
    
    global user_history

    existing_entry = user_history[
        (user_history['username'] == username) & (user_history['set_id'] == int(set_id))
    ]

    if not existing_entry.empty:
        user_history.loc[
            (user_history['username'] == username) & (user_history['set_id'] == int(set_id)),
            'times_completed'
        ] += 1
    else:
        new_entry = pd.DataFrame([{
            "username": username,
            "set_id": int(set_id),
            "times_completed": 1
        }])
        user_history = pd.concat([user_history, new_entry], ignore_index=True)

    
    user_history.to_csv(user_history_file, index=False)

    return jsonify({"message": "History updated"}), 200

if __name__ == "__main__":
    app.run(debug=True)