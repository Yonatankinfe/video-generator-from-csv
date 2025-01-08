import cv2
import csv
import numpy as np

# Read video properties from CSV file
csv_file = 'properties.csv'  # Replace with your actual CSV file path
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    properties = next(reader)

# Extract properties
timeline = int(properties['Timeline'])
frame_rate = int(properties['Frame rate'])
resolution = tuple(map(int, properties['Resolution'].split('x')))
bitrate = int(properties['Bitrate'])
codec = cv2.VideoWriter_fourcc(*properties['Video codec'])
duration_frames = int(properties['Duration in frames'])
font_scale_title = float(properties['Title font scale'])
font_scale_subtitle = float(properties['Subtitle font scale'])
font_color = int(properties['Font color'])
background_gradient = int(properties['Background gradient'])

# Set up video writer
output_file = 'output_video.mp4'
video_writer = cv2.VideoWriter(output_file, codec, frame_rate, resolution)

# Generate frames
for i in range(duration_frames):
    # Create gradient background
    gradient = np.linspace(background_gradient, font_color, resolution[0], dtype=np.uint8)
    frame = np.tile(gradient, (resolution[1], 1, 1))
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    # Add title text
    title_text = "Sample Video Title"
    subtitle_text = "Subtitle Text"
    org_title = (50, 100)  # Position of title text
    org_subtitle = (50, 150)  # Position of subtitle text

    cv2.putText(frame, title_text, org_title, cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale_title, (font_color, font_color, font_color), 2, cv2.LINE_AA)
    cv2.putText(frame, subtitle_text, org_subtitle, cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale_subtitle, (font_color, font_color, font_color), 1, cv2.LINE_AA)

    # Write frame to video
    video_writer.write(frame)

# Release the video writer
video_writer.release()
print(f"Video saved as {output_file}")
