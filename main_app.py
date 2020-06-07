from time import sleep
import pandas as pd
import xlrd
import os
import datetime
from flask import Flask, render_template, request, Response, url_for, redirect, send_file
from werkzeug.utils import secure_filename
"""import your script modules
from scripts.<library> import <resource>
"""
app = Flask(__name__)
app_name = 'Automate_with_python_excel'

# Create a directory in a known location to save excel files to.
uploads_dir = os.path.join(app.instance_path, 'uploads')
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

# Create a directory in a known location to save result files to.
export_result_dir = os.path.join(app.instance_path, 'results')
if not os.path.exists(export_result_dir):
    os.makedirs(export_result_dir)

# Global variables to be tuned
global_df = pd.DataFrame()
global_filename = ''
sheet_names = list()
actions_list = ['config', 'delete']
global_result = ''
selected_action = ''

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/upload_file.html', methods=['GET', 'POST'])
def upload():
    global global_df, global_filename, sheet_names
    if request.method == 'POST':
        f = request.files['inputFile']

        filename_path_saved = os.path.join(uploads_dir, secure_filename(f.filename))
        print(filename_path_saved)
        f.save(filename_path_saved)
        global_filename = filename_path_saved
        
        xls = xlrd.open_workbook(global_filename, on_demand=True)
        sheet_names = xls.sheet_names()
        nSheets = len(sheet_names)

        return render_template('upload_file.html', filename=global_filename, excel_sheet_list=sheet_names)
    if global_df.empty:
        return render_template('upload_file.html')
    else:
        return render_template('upload_file.html', filename=global_filename, excel_sheet_list=sheet_names, tables=[global_df.to_html(classes='data')])
        
@app.route('/Load_Data', methods=['GET', 'POST'])
def load_data():
    global global_df, global_filename, sheet_names
    if request.method == 'POST':
        selected_sheet = str(request.form['excel_sheet'])
        print(selected_sheet)
        data_xls = pd.read_excel(global_filename, selected_sheet)
        global_df = data_xls.copy()

        sheet_names.remove(selected_sheet)

        sheet_names.insert(0,selected_sheet)

        return render_template('upload_file.html', tables=[global_df.to_html(classes='data')], filename=global_filename, excel_sheet_list=sheet_names)
    if global_df.empty:
        return render_template('upload_file.html')
    else:
        return render_template('upload_file.html', filename=global_filename, excel_sheet_list=sheet_names, tables=[global_df.to_html(classes='data')])

@app.route('/action.html')
def action():
    global actions_list
    return render_template('action.html', action_list=actions_list, result=global_result)

@app.route('/Config_Delete_Action', methods=['GET', 'POST'])
def config_delete_action():
    global actions_list, global_result, global_df, selected_action
    if request.method == 'POST':
        selected_action = str(request.form['action'])
        print(selected_action)
        
        actions_list.remove(selected_action)
        
        actions_list.insert(0,selected_action)
        
        if selected_action == 'config':
            global_result = 'Add your scripts for configuration'
        elif selected_action == 'delete':
            global_result = 'Add your scripts for deletion'
        else:
            global_result = ''
    return render_template('action.html', action_list=actions_list, result=global_result)

@app.route('/Export_Result', methods=['GET', 'POST'])
def export_result():
	global global_result, selected_action
	if (global_result != '' and selected_action != ''):
		if request.method == 'POST':
			filename=secure_filename('{}_{}_{}.txt'.format(app_name, selected_action, datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
			result_file_path = os.path.join(export_result_dir, filename)
			f = open(result_file_path, 'w')
			f.write(global_result)
			f.close()
		return send_file(result_file_path,
						 mimetype='text',
						 attachment_filename=filename,
						 as_attachment=True)
	else:
		return render_template('action.html', action_list=actions_list, result=global_result)

@app.route('/settings.html')
def settings():
    return render_template('settings.html')

@app.route('/Reset_Application', methods=['GET', 'POST'])
def reset_application():
    global actions_list, global_result, global_df, sheet_names, selected_action
    if request.method == 'POST':
        global_df = pd.DataFrame()
        global_filename = ''
        sheet_names = list()
        actions_list = ['config', 'delete']
        global_result = ''
        selected_action = ''
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
