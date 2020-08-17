#!/bin/bash)

for music in ls musicas_mp4/*.mp4; do
	# echo "${music%.mp4}"
	# echo "ffmpeg -i" "$music" "./musicas_mp3/${music%.mp4}.mp3"
	ffmpeg -i "$music" "./musicas_mp3/${music%.mp4}.mp3"
done

# for f in *.txt; do 
    # mv -- "$f" "${f%.txt}.text"
# done
