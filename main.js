console.log('Tuki')
const synth = new Tone.PolySynth(Tone.Synth).toDestination();

async function generateAndPlay() {
    try {
        // Ensure audio context is running
        //await Tone.start();

        // Fetch sequence from backend
        const response = await axios.get('http://localhost:5000/generate_sequence');
        const sequence = response.data;
        console.log(sequence);

        // Stop any ongoing playback
        Tone.Transport.stop();
        Tone.Transport.cancel();

        // Schedule new sequence
        let startTime = Tone.now();
        sequence.forEach((noteData, index) => {
            const { note, velocity, duration } = noteData;
            const time = startTime + index * duration;
            
            synth.triggerAttackRelease(
                Tone.Frequency(note, "midi"),
                duration,
                time,
                velocity / 127  // Normalize velocity to 0-1 range
            );
        });

        // Start playback
        Tone.Transport.start();

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Check the console for details.');
    }
}