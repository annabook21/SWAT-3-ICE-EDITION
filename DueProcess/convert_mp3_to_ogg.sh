#!/bin/bash

# MP3 to OGG Converter for SWAT 4
# Usage: ./convert_mp3_to_ogg.sh [folder]
# If no folder specified, converts all MP3s in current directory

FOLDER="${1:-.}"

echo "Converting MP3 files in: $FOLDER"
echo "================================"

count=0
for f in "$FOLDER"/*.mp3; do
    [ -e "$f" ] || continue
    
    basename="${f%.mp3}"
    filename=$(basename "$basename")
    
    echo "Converting: $filename.mp3"
    
    # Convert to WAV first (mono, 44100 Hz)
    ffmpeg -i "$f" -ac 1 -ar 44100 "${basename}_temp.wav" -y -loglevel error
    
    # Encode to OGG Vorbis
    oggenc -q 4 "${basename}_temp.wav" -o "${basename}.ogg" --quiet
    
    # Clean up temp file
    rm "${basename}_temp.wav"
    
    ((count++))
done

echo "================================"
echo "Done! Converted $count files."
