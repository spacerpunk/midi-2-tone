from flask import Flask, jsonify
from flask_cors import CORS
import random
import mingus.core.scales as scales
from mingus.containers import Note

app = Flask(__name__)
CORS(app)

# Global variables
bpm = 60 / 100
notes = ["C", "D", "E", "F", "G", "A", "B"]

@app.route('/generate_sequence')
def generate_sequence():
    # Generate and return the MIDI sequence
    sequence = generate_midi_sequence()
    return jsonify(sequence)

def generate_midi_sequence():
    # Initialize scales
    ionian = scales.Ionian(notes[random.randrange(0, len(notes))])
    aeolian = scales.Aeolian(notes[random.randrange(0, len(notes))])
    naturalMinor = scales.NaturalMinor(notes[random.randrange(0, len(notes))])
    scales_list = [ionian, aeolian, naturalMinor]

    # Convert Mingus notation to MIDI notation
    notesArray = convert_notes(scales_list)

    # Generate sequence
    sequence = []
    for _ in range(10):  # Generate 10 notes
        note = notesArray[random.randrange(0, len(notesArray))]
        velocity = random.randrange(35, 100)
        duration = bpm * 4  # Duration in seconds
        sequence.append({
            "note": note,
            "velocity": velocity,
            "duration": duration
        })

    return sequence

def convert_notes(scales_list):
    notesArray = []
    scale = scales_list[random.randrange(0, len(scales_list))]
    print(f"Selected scale: {scale}")
    for note in scale.ascending():
        n = int(Note(note, random.randrange(4, 5)))
        notesArray.append(n)
    return notesArray

if __name__ == '__main__':
    app.run(debug=True)