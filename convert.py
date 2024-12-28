import pydot

def convert_dot_to_png(dot_file, png_file):
    # Load the .dot file
    (graph,) = pydot.graph_from_dot_file(dot_file)

    # Save it as a PNG file
    graph.write_png(png_file)

# Specify the input and output file names
dot_file = '/home/ziuteng/Python_AI_for_beginner/student_per.dot'  # Replace with your .dot file name
png_file = 'output_graph6.png'  # Desired output .png file name

# Convert the file
convert_dot_to_png(dot_file, png_file)