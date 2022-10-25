import pandas as pd
import os
import statistics # statistics.mean, statistics.stdev, statistics.median

TIME_SLICE = 1

cols = ['mean_x', 'std_x', 'median_x', 'rms_x', 'mean_y', 'std_y', 'median_y', 'rms_y','mean_z', 'std_z', 'median_z', 'rms_z','Activity'] 

def rms(vals):
    sq_vals = [val**2 for val in vals]
    return statistics.mean(sq_vals)**0.5


def features(entries):
    df_final = pd.DataFrame(columns=cols)

    for entry in entries:
        if (".DS_Store" in entry): continue

        df = pd.read_csv('formatted_data/' + entry, header=None) 
        num_entries = df.shape[0]

        activity = 'not_hand_wash' if ('NonHandWash' in entry) else 'hand_wash'


        # Find duration of sensor readings in seconds: (end_timestamp-start_timestamp)/1000
        num_seconds = int((df.iloc[-1,0] - df.iloc[0,0])/1000)

        # Find number of entires corresponding to one second; i.e., num_entries/num_seconds); Instructions say to ignore last <1 second data
        window_size = int(num_entries/num_seconds)
        print("window=" + str(window_size))

        df_features = pd.DataFrame(columns=cols)

        # calculate features for each second's worth of data
        for i in range (0, num_seconds-TIME_SLICE + 1):
            start = i*window_size
            end   = start+window_size*TIME_SLICE
            x_accel = df.iloc[start:end,1]
            y_accel = df.iloc[start:end,2]
            z_accel = df.iloc[start:end,3]

            values = pd.DataFrame(
            {
                "mean_x": [statistics.mean(x_accel)],
                "std_x":  [statistics.stdev(x_accel)],
                "median_x":  [statistics.median(x_accel)],
                "rms_x":  [rms(x_accel)],
                "mean_y": [statistics.mean(y_accel)],
                "std_y":  [statistics.stdev(y_accel)],
                "median_y":  [statistics.median(y_accel)],
                "rms_y":  [rms(y_accel)],
                "mean_z": [statistics.mean(z_accel)],
                "std_z":  [statistics.stdev(z_accel)],
                "median_z":  [statistics.median(z_accel)],
                "rms_z":  [rms(z_accel)],
                "Activity": activity
            }
            )

            df_features = pd.concat([df_features, values])
            print(str(start) + " " + str(end))

        print(entry)
        print(df_features)
        df_final = pd.concat([df_final, df_features])

    print(df_final)
    df_final.to_csv('./features.csv', encoding='utf-8', index=False, header=True)


def main():
    entries = os.listdir('formatted_data/')
    features(entries)

if __name__ == "__main__":
    main()
