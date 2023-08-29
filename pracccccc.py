
import pandas as pd
import plotly.graph_objects as go

# Read data from an Excel file
data_file = pd.read_excel(r'C:\Users\Adavi Sarvan-3316\PycharmProjects\pythontesting\Assignments\heatmap_data.xlsx')  # Replace with your file path

# Define labels, values, and colors based on the columns in your Excel file
labels = data_file['label'].tolist()
values = data_file['index'].tolist()
colors = data_file['colors'].tolist()  # Assuming the 'colors' column contains color names or RGB values

# Create a treemap figure
fig = go.Figure(go.Treemap(
    labels=labels,
    parents=[''] * len(labels),
    values=values,
    texttemplate="%{label}<br>%{value}",
    textfont={"size": 15},
    hoverinfo="text",
    marker=dict(
        colors=colors  # Assign colors based on the 'colors' column
    )
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

# Display the treemap
fig.show()
