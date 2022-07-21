from flask import Flask, render_template, request,redirect,url_for
from flask import *
import os
from matplotlib.pyplot import title
import pandas as pd
# import matplotlib.pyplot as plt
import datetime
import glob
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app=Flask(__name__)
# data1=pd.DataFrame()
# data2=pd.DataFrame()
# occur=pd.DataFrame()
# sla=pd.DataFrame()
# data1=pd.read_csv('static/DefectsData.csv')
# data2=pd.read_csv('static/Objective OWASP Top 10 (2017).csv')
# occur=pd.read_csv('static/security.csv')
# overdue_df1=pd.DataFrame
# overdue_df2=pd.DataFrame
# string_seg=""

# sla=pd.read_csv('static/SLA.csv')
expired=[]
non_expired= []
# file1=False
# file2=False
# file3=False
# file4=False
seg1={}
msg=""
date_today=str(datetime.date.today())
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method =='POST':
        file1=request.files['defectscsvfile']
        file2=request.files['securitycsvfile']
        file3=request.files['coveritycsvfile']
        file4=request.files['slacsvfile']
        
        if file1:
            files_a = glob.glob('static/defects/*')   
            for f in files_a:
                os.remove(f)
            filepath1=os.path.join('static/defects',file1.filename)
            file1.save(filepath1)
        if file2:
            files_b = glob.glob('static/security/*')   
            for f in files_b:
                os.remove(f)
            filepath2=os.path.join('static/security',file2.filename)
            file2.save(filepath2)
        if file3:
            files_c = glob.glob('static/coverity/*')   
            for f in files_c:
                os.remove(f)
            filepath3=os.path.join('static/coverity',file3.filename)
            file3.save(filepath3)
        if file4:
            files_d = glob.glob('static/sla/*')   
            for f in files_d:
                os.remove(f)
            filepath4=os.path.join('static/sla',file4.filename)
            file4.save(filepath4)
        if not os.path.isdir('static'):
            os.mkdir('static')

        print(file1.filename)
        print(file2.filename)
        print(file3.filename)
        print(file4.filename)

    # l=[]        
    # for i in range(data1.shape[0]):
    #     dateA=str(date_today)             
    #     dateA=dateA.split("-")
    #     dateA=datetime.date(int(dateA[0]),int(dateA[1]),int(dateA[2]))
    #     dateB=(data1['Created_date'][i])
    #     dateB=dateB.split("-")
    #     dateB=datetime.date(int(dateB[2]),int(dateB[1]),int(dateB[0]))
    #     l.append((dateA-dateB).days)
    # data1[str(date_today)]=l
    
    # l2=[]
    # for i in range(data2.shape[0]):
    #     dateX=str(date_today)             
    #     dateX=dateX.split("-")
    #     dateX=datetime.date(int(dateX[0]),int(dateX[1]),int(dateX[2]))
    #     dateY=(data2['First Detected'][i])
    #     dateY=dateY.split("-")
    #     dateY=datetime.date(int(dateY[2]),int(dateY[1]),int(dateY[0]))
    #     l2.append((dateX-dateY).days)
    # data2[str(date_today)]=l2

    # exp=[]
    # for j in range(sla.shape[0]):
    #     # if(data1['CVSS'][i]>=sla['SB'][j] and data1['CVSS'][i]<=sla['SE'][j]):
    #     string_seg=str(sla['SB'][j])+ " - " +str(sla['SE'][j])
    #     seg1.update({str(string_seg):0})
    # for i in range(data1.shape[0]):
    #     for j in range(sla.shape[0]):
    #         if(data1['CVSS'][i]>=sla['SB'][j] and data1['CVSS'][i]<=sla['SE'][j]):
    
    #             string_seg=str(sla['SB'][j])+ " - " +str(sla['SE'][j])
    #             if string_seg in seg1:
    #                 seg1[str(string_seg)]+=1
    #              #print("DEBUG")
    #             else:
    #                 seg1.update({string_seg:1})           
    #             if(sla['Duration'][j]<data1[str(date_today)][i]):
    #                 exp.append("Over Due")
    #             else:
                    
    #                 exp.append("On Time")
    
    # #print(seg1)
    # data1["overdue"]=exp
    # data1.sort_values(by=str(date_today) ,ascending=False,inplace=True)

    # exp2=[]
    # for j in range(sla.shape[0]):
    #     if(6.8>=sla['SB'][j] and 6.8<=sla['SE'][j]):
    #         age2=sla['Duration'][j]
    # # print("age2= ",age2)
    
    # for i in range(data2.shape[0]):
    #     if(data2[str(date_today)][i]<age2):
    #         exp2.append("Over Due")
    #     else:
    #         exp2.append("On Time")
    # data2["overdue"]=exp2
    
    # data2.sort_values(by=str(date_today) ,ascending=False,inplace=True)
    
    return render_template('index.html',msg=msg)
    

data3=pd.DataFrame
data4=pd.DataFrame

@app.route('/table')
def table():
    try:
        file_def=False
        files_defects = glob.glob('static/defects/*')   
        for f in files_defects:
            file_def=f
        file_s=False
        files_sla = glob.glob('static/sla/*')   
        for f in files_sla:
            file_s=f
        if (not file_s) and (not file_def):
            msg="Upload both deffects and SLA data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        if not file_s:
            msg="Upload SLA data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        if not file_def:
            msg="Upload deffects data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        sla=pd.read_csv(str(file_s))
        data1=pd.read_csv(str(file_def))
        l=[]        
        for i in range(data1.shape[0]):
            dateA=str(date_today)             
            dateA=dateA.split("-")
            dateA=datetime.date(int(dateA[0]),int(dateA[1]),int(dateA[2]))
            dateB=(data1['Created_date'][i])
            dateB=dateB.split("-")
            dateB=datetime.date(int(dateB[2]),int(dateB[1]),int(dateB[0]))
            l.append((dateA-dateB).days)
        data1[str(date_today)]=l
        exp=[]
        for j in range(sla.shape[0]):
            # if(data1['CVSS'][i]>=sla['SB'][j] and data1['CVSS'][i]<=sla['SE'][j]):
            string_seg=str(sla['SB'][j])+ " - " +str(sla['SE'][j])
            seg1.update({str(string_seg):0})
        for i in range(data1.shape[0]):
            for j in range(sla.shape[0]):
                if(data1['CVSS'][i]>=sla['SB'][j] and data1['CVSS'][i]<=sla['SE'][j]):
        
                    string_seg=str(sla['SB'][j])+ " - " +str(sla['SE'][j])
                    if string_seg in seg1:
                        seg1[str(string_seg)]+=1
                    #print("DEBUG")
                    else:
                        seg1.update({string_seg:1})           
                    if(sla['Duration'][j]<data1[str(date_today)][i]):
                        exp.append("Over Due")
                    else:
                        
                        exp.append("On Time")
        
        #print(seg1)
        data1["overdue"]=exp
        data1.sort_values(by=str(date_today) ,ascending=False,inplace=True)


        data3=data1[['ID','Title','CVSS','Created_date','overdue']]
        # print(data3)
        table1=data3.to_numpy()
        df4=data3['overdue'].value_counts()
        df4=df4.to_dict()
        # print(df4)
        overdue_df1=data1[data1["overdue"]=="Over Due"]
        data3=data3[data3["overdue"]=="On Time"]
        print(seg1)

        return render_template('table.html',tables=data3,df=df4,table_od1=overdue_df1,sd=seg1)
    except:
        msg="File format may be wrong"
        return render_template("error.html",msg=msg)
    



@app.route('/table2')
def table2():
    try:
        file_occ=False
        files_occur = glob.glob('static/security/*')   
        for f in files_occur:
            file_occ=f
        if not file_occ:
            msg="Upload Security data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        occur=pd.read_csv(str(file_occ))
        sec={}
        for i in range(occur.shape[0]):
            if(occur['AWS Account'][i] in sec):
                sec[str(occur['AWS Account'][i])][0]+=occur['Security Score'][i]
                sec[str(occur['AWS Account'][i])][1]+=1
            else:
                p=[]
                p.append(occur['Security Score'][i])
                p.append(1)
                sec.update({str(occur['AWS Account'][i]): p})
        sec2={}
        for i in sec:
            sec2.update({i:sec[i][0]/sec[i][1]})
        # print(sec2)

        return render_template('table2.html',scores=sec2)
    except:
        msg="File format may be wrong"
        return render_template("error.html",msg=msg)

@app.route('/coverity')
def coverity():
    try:
        file_cov=False
        files_coverity = glob.glob('static/coverity/*')   
        for f in files_coverity:
            file_cov=f
        # if not file_cov:
        #     return render_template("error.html")
        file_s=False
        files_sla = glob.glob('static/sla/*')   
        for f in files_sla:
            file_s=f
        if (not file_s) and (not file_cov):
            msg="Upload both Coverity and SLA data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        if not file_s:
            msg="Upload SLA data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        if not file_cov:
            msg="Upload Coverity data"
            # flash(msg,'error')
            # return redirect(url_for("index"))
            return render_template("error.html",msg=msg)
        
        
        data2=pd.read_csv(str(file_cov))
        sla=pd.read_csv(str(file_s))
        l2=[]
        for i in range(data2.shape[0]):
            dateX=str(date_today)             
            dateX=dateX.split("-")
            dateX=datetime.date(int(dateX[0]),int(dateX[1]),int(dateX[2]))
            dateY=(data2['First Detected'][i])
            dateY=dateY.split("-")
            dateY=datetime.date(int(dateY[2]),int(dateY[1]),int(dateY[0]))
            l2.append((dateX-dateY).days)
        data2[str(date_today)]=l2
        exp2=[]
        for j in range(sla.shape[0]):
            if(6.8>=sla['SB'][j] and 6.8<=sla['SE'][j]):
                age2=sla['Duration'][j]
        # print("age2= ",age2)
        
        for i in range(data2.shape[0]):
            if(data2[str(date_today)][i]<age2):
                exp2.append("Over Due")
            else:
                exp2.append("On Time")
        data2["overdue"]=exp2
        data2.sort_values(by=str(date_today) ,ascending=False,inplace=True)


        df1=data2['Team Backlog'].value_counts()
        # print(df1)
        df1=df1.to_dict()
        da1=data2['Dashboard Category'].value_counts()
        da1=da1.to_dict()
        data4=data2[['Dashboard Category','CID','ART','Team Backlog','Severity','Type','Category','CWE','Checker','Action','File','External Reference','Baseline','First Detected','overdue']]
        # print(data4)
        data4=data4.sort_values(by="Dashboard Category")
        table2=data4.to_numpy()
        # print(table2)
        df5=data4['overdue'].value_counts()
        # print(df5)
        df5=df5.to_dict()
        overdue_df2=data4[data4["overdue"]=="Over Due"]
        data4=data4[data4["overdue"]=="On Time"]
        return render_template('coverity.html',df=df1,da=da1,tables=data4,od=df5,table_od2=overdue_df2)
    except:
        msg="File format may be wrong"
        return render_template("error.html",msg=msg)
    
#   return render_template('table2.html',scores=sec2)

# @app.route('/error')
# def error():
#     return render_template('error.html')
if  __name__=='__main__':
    app.run(debug=True)