import pandas as pd  

total_r0 = 0

for i in range(1, 4):
    df_sdp = pd.read_csv(f'jgroups_sdp_test_commit_seed{i}.csv')
    df_pre = pd.read_csv(f'jgroups_test_pre_seed{i}.csv')

    df_pass = df_pre[df_pre['status'] == 0]

    not_matching_commit_ids = ~df_pass['commit_id'].isin(df_sdp['commit_id'])

    proportion = not_matching_commit_ids.sum() / len(df_pass)

    total_r0 += proportion


#print("average testing recall 0:" + str(total_r0/3))
print("average testing false alarm:" + str(1-total_r0/3))
