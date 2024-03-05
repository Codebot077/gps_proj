import pandas as pd
from geopy.distance import geodesic


file_path = r'output_coordinates.csv'
df = pd.read_csv(file_path)


# Remove the last part from each entry in the 'timestamp' column
df['Timestamp'] = df['Timestamp'].apply(lambda x: x.split()[0])

def calculate_velocity(coord1, coord2, time1, time2):
    distance = geodesic(coord1, coord2).kilometers
    time_diff = (time2 - time1).total_seconds() / 3600  # Convert seconds to hours
    # print(time_diff)
    velocity = distance / time_diff
    return velocity,distance

# Initialize an empty list to store the results
results = []

initial_speed = 0

for i in range(20, len(df), 20):
    coord1 = (df['Latitude'].iloc[i-20], df['Longitude'].iloc[i-20])
    coord2 = (df['Latitude'].iloc[i], df['Longitude'].iloc[i])
    time1 = pd.to_datetime(df['Timestamp'].iloc[i-20], format='%H:%M:%S')
    time2 = pd.to_datetime(df['Timestamp'].iloc[i], format='%H:%M:%S')

    velocity, distance = calculate_velocity(coord1, coord2, time1, time2)
    acceleration = (velocity - initial_speed) / (time2 - time1).total_seconds()
    initial_timestamp = df['Timestamp'].iloc[i-20]
    final_timestamp = df['Timestamp'].iloc[i]

    # Append the results to the list
    results.append({'Initial Time': initial_timestamp,
                    'Final Time': final_timestamp,
                    'Speed': velocity,
                    'Distance': distance,
                    'Acceleration': acceleration})
    
    # Update the initial speed for the next iteration
    initial_speed = velocity


# Create a DataFrame from the list of dictionaries
results_df = pd.DataFrame(results)


# Save the results to a CSV file
results_df.to_csv('output_results.csv', index=False)

print(results_df)
print("Total distance travelled:", round(results_df['Distance'].sum(),2),'Km')
print("Highest speed reached:",round(results_df['Speed'].max(),2),'Km/hr')


# Find the row with the highest acceleration
max_accel_row = results_df.loc[results_df['Acceleration'].idxmax()]

# Extract the initial and final timestamps from the row
initial_time_max_accel = max_accel_row['Initial Time']
final_time_max_accel = max_accel_row['Final Time']

# Print the highest acceleration achieved and the corresponding timeframe
print("Highest acceleration achieved:", round(max_accel_row['Acceleration'], 2),"during the timeframe:", initial_time_max_accel, "to", final_time_max_accel)



