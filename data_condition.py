import pandas as pd
import os
from pathlib import Path
from datetime import datetime



def filter_data(file_name, list_row_1, list_row_2, list_row_3, list_row_4,base):
    excel_path = file_name
    folder_path = os.path.dirname(Path(excel_path))
    inp_file_name = os.path.basename(excel_path)
    opt_ext  = inp_file_name.split('.')[0]
    output_path = os.path.join(folder_path, opt_ext+'_output.xlsx')

    data = pd.read_excel(excel_path)
    # values for user input row 1
    v1s1 = float(list_row_1[0])
    v2s1 = float(list_row_1[1])
    v3s1 = float(list_row_1[2])
    v4s1 = float(list_row_1[3])
    # values for user input row 2
    v1s2 = float(list_row_2[0])
    v2s2 = float(list_row_2[1])
    v3s2 = float(list_row_2[2])
    v4s2 = float(list_row_2[3])
    # values for user input row 3
    v1s3 = float(list_row_3[0])
    v2s3 = float(list_row_3[1])
    v3s3 = float(list_row_3[2])
    v4s3 = float(list_row_3[3])
    # values for user input row 4
    v1s4 = float(list_row_4[0])
    v2s4 = float(list_row_4[1])
    v3s4 = float(list_row_4[2])
    v4s4 = float(list_row_4[3])
    todays_date = datetime.now()
    # current_timestamp = todays_date.strftime("%Y-%m-%d %H:%M:%S")
    # current_date, current_time = current_timestamp.split(' ')
    # print(current_date, current_time)
    df_list = []
    for i in range(0,data.shape[0]):
        base.update_idletasks()
        j = 0
        filt_df = data[0+i:5+i]
        if filt_df.shape[0] ==5:
            filt_df = filt_df.reset_index()
            # if ((filt_df['Value 1'][0] <= v1s1 < filt_df['Value 1'][1]) and (filt_df['Value 2'][0] >= v2s1 > filt_df['Value 2'][1]) and (filt_df['Value 3'][0] >= v3s1 >filt_df['Value 3'][1]) and  (filt_df['Value 4'][0] >= v4s1 > filt_df['Value 4'][1])) and ((filt_df['Value 1'][1] >= v1s2 > filt_df['Value 1'][2]) and (filt_df['Value 2'][1] <= v2s2 < filt_df['Value 2'][2]) and (filt_df['Value 3'][1] >=v3s2 > filt_df['Value 3'][2]) and (filt_df['Value 4'][1] >= v4s2 > filt_df['Value 4'][2])) and ((filt_df['Value 1'][2] <= v1s3 < filt_df['Value 1'][3]) and (filt_df['Value 2'][2] >=v2s3 > filt_df['Value 2'][3]) and (filt_df['Value 3'][2] >= v3s3 > filt_df['Value 3'][3]) and (filt_df['Value 4'][2] >= v4s3 > filt_df['Value 4'][3])) and ((filt_df['Value 1'][3] >= v1s4 > filt_df['Value 1'][4]) and (filt_df['Value 2'][3] <= v2s4 < filt_df['Value 2'][4]) and (filt_df['Value 3'][3] >= v3s4 > filt_df['Value 3'][4]) and (filt_df['Value 4'][3] >= v4s4 > filt_df['Value 4'][4])):
            # new condition
            if ((filt_df['Value 1'][0] <= v1s1 < filt_df['Value 1'][1]) and (filt_df['Value 2'][0] <= v2s1 < filt_df['Value 2'][1]) and (filt_df['Value 3'][0] <= v3s1 < filt_df['Value 3'][1]) and (filt_df['Value 4'][0] <= v4s1 < filt_df['Value 4'][1])) and ((filt_df['Value 1'][1] <= v1s2 < filt_df['Value 1'][2]) and (filt_df['Value 2'][1] <= v2s2 < filt_df['Value 2'][2]) and (filt_df['Value 3'][1] <= v3s2 < filt_df['Value 3'][2]) and (filt_df['Value 4'][1] <= v4s2 < filt_df['Value 4'][2])) and ((filt_df['Value 1'][2] <= v1s3 < filt_df['Value 1'][3]) and (filt_df['Value 2'][2] >= v2s3 > filt_df['Value 2'][3]) and (filt_df['Value 3'][2] >= v3s3 > filt_df['Value 3'][3]) and (filt_df['Value 4'][2] >= v4s3 > filt_df['Value 4'][3])) and ((filt_df['Value 1'][3] <= v1s4 < filt_df['Value 1'][4]) and (filt_df['Value 2'][3] <= v2s4 < filt_df['Value 2'][4]) and (filt_df['Value 3'][3] <= v3s4 < filt_df['Value 3'][4]) and (filt_df['Value 4'][3] <= v4s4 < filt_df['Value 4'][4])):
                
                # filt_df['Date'] = current_date
                # filt_df['Time'] = current_time
                if 'index' in filt_df.columns:
                    filt_df.drop(['index'], axis=1, inplace=True)
                df_list.append(filt_df)
       
    if len(df_list)>0:
        final_df = pd.concat(df_list, ignore_index=True)
    else:
        final_df = pd.DataFrame()
    final_df.to_excel(output_path)
    return final_df, output_path

if __name__ == '__main__':
    pass
    # v1s1 = -0.04
    # v2s1 = -0.036
    # v3s1 = -0.036
    # v4s1 = -0.036

    # v1s2 = -0.034
    # v2s2 = -0.033
    # v3s2 = -0.034
    # v4s2 = -0.033

    # v1s3 = -0.033
    # v2s3 = -0.032
    # v3s3 = -0.03
    # v4s3 = -0.03

    # v1s4 = -0.031
    # v2s4 = -0.032
    # v3s4 = -0.031
    # v4s4 = -0.030
    # r1_list = [v1s1,v2s1, v3s1,v4s1]
    # r2_list = [v1s2,v2s2, v3s2,v4s2]
    # r3_list = [v1s3,v2s3, v3s3,v4s3]
    # r4_list = [v1s4,v2s4, v3s4,v4s4]
    # file = r"C:\Users\sarwa\Desktop\DATA_FILTER\1672916981-test.xlsx"
    # result = filter_data(file, r1_list, r2_list, r3_list, r4_list)

            
        
        