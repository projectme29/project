from flask import Flask, render_template, request, url_for
import pandas as pd
import csv
app=Flask(__name__)
app.secret_key="thisiskey"

col_names = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]
col_types = ["int","text","text","text","int",
    "int","int","int","int","int","int",
    "int","int","int","int","int",
    "int","int","int","int",
    "int","int","int","int","int",
    "int","int","int","int",
    "int","int","int","int",
    "int","int","int",
    "int","int","int",
    "int","int","text"]

sel_names = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","label"]
sel_types = ["int","text","text","text","int",
    "int","text"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dataset')
def dataset():
    length=len(col_names)
    kdd_data = pd.read_csv("dataset/kddtop25000", header=None, names=col_names)
    return render_template('dataset.html',len=length,kdd_data=col_names,types=col_types)

@app.route('/feature selection')
def featureselection():
    length=len(sel_names)
    kdd_data = pd.read_csv("dataset/kddtop25000", header=None, names=sel_names)
    return render_template('featureselection.html',len=length,kdd_data=sel_names,types=sel_types)

@app.route('/classfication')
def classification():
    length=len(col_names)
    kdd_data = pd.read_csv("dataset/kddtop25000", header=None, names=col_names)
    return render_template('classification.html',len=length,kdd_data=col_names,types=col_types)

@app.route('/prediction')
def prediction():

    return render_template('prediction.html')

@app.route('/analysis')
def analysis():
    length=len(col_names)
    kdd_data = pd.read_csv("dataset/kddtop25000", header=None, names=col_names)
    return render_template('analysis.html',len=length,kdd_data=col_names,types=col_types)

@app.route('/dtree')
def dtree():

    return render_template('dtree.html')

@app.route('/rf')
def rf():

    return render_template('rf.html')

@app.route('/kmeans')
def kmeans():

    return render_template('kmeans.html')

@app.route('/mlp')
def mlp():

    return render_template('mlp.html')

if __name__ == '__main__':
    app.run(debug=True)