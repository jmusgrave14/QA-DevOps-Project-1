from flask import Flask, request
from backup import backup_folder
from backup import backup_file
from data import get_log, get_stat
from os import path

app = Flask(__name__)


@app.route('/log')
def log():
    try:
        start = request.args.get('start')
        end = request.args.get('end')

        logs = get_log(start, end)
        response = logs
        return response
    except ValueError:
        response = "Invalid Dates"
        return response, 400


@app.route('/stat')
def stat():
    stats = get_stat()
    response = stats
    return response 


@app.route('/', methods=['POST'])
def backup():  # put application's code here

    folderorfile_to_backup = request.json["path"]
    try:
        if folderorfile_to_backup is None:
            response = "No folder or file path supplied"
            return response, 400

        if path.isdir(folderorfile_to_backup) == True:
            backup_folder(folderorfile_to_backup)
            response = "Backup Completed"
            return response, 201

        elif path.isfile(folderorfile_to_backup) == True:
            backup_file(folderorfile_to_backup)
            response = "Backup Completed"
            return response, 201
    except ValueError:
        response = "No such folder or file: " + folderorfile_to_backup
        return response, 404


# Run Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0')
