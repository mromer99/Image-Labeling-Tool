from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import json

app = Flask(__name__)

images_path = './all_datasets/images'
labels_path = './all_datasets/labels'

@app.route('/')
def index():
    image_files = os.listdir(images_path)
    labels_files = os.listdir(labels_path)

    images = []
    for image_file in image_files:
        labels_file = os.path.splitext(image_file)[0] + '.txt'
        if labels_file in labels_files:
            with open(os.path.join(labels_path, labels_file), 'r') as f:
                labels = f.read().strip().split('\n')
                labels = [list(map(float, label.split())) for label in labels]
        else:
            labels = []

        images.append({'name': image_file, 'labels': labels})

    return render_template('gallery.html', images=images)


@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(images_path, filename)


@app.route('/save-coordinates/<filename>', methods=['POST'])
def save_coordinates(filename):
    print('Received save-coordinates request')  
    data = request.get_json()
    labels_file = os.path.splitext(filename)[0] + '.txt'

    # Read the existing labels
    with open(os.path.join(labels_path, labels_file), 'r') as f:
        labels = [list(map(float, line.split())) for line in f.read().split('\n') if line]

    # Update the label at the given index with the new coordinates
    labels[data['index']] = data['labels']

    # Write the updated labels back to the file
    with open(os.path.join(labels_path, labels_file), 'w') as f:
        for label in labels:
            f.write(' '.join(map(str, label)) + '\n')

    return jsonify({'status': 'success'})


@app.route('/replace-labels/<filename>', methods=['POST'])
def replace_labels(filename):
    new_labels = request.json['labels']
    if not new_labels:
        return jsonify({'status': 'failed', 'message': 'No labels to save'})
    labels_file = os.path.splitext(filename)[0] + '.txt'
    with open(os.path.join(labels_path, labels_file), 'w') as f:
        for label in new_labels:
            f.write(' '.join(map(str, label)) + '\n')
    return jsonify({'status': 'success'})



if __name__ == '__main__':
    app.run(debug=True)