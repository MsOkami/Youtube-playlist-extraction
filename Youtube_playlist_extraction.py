from pytubefix import Playlist # Import the playlist class from the pytube library
import sys # Import the sys module for system-specific parameters and functions

playlist_url = 'https://www.youtube.com/playlist?list=PL23DNUEsneQ-zOR9qGMTjs3BlZIOv6Vzj'
try:
    print(f"fetching Playlist Info from youtube {playlist_url}")
    p = Playlist(playlist_url)
    # Print the title of the playlist to comfirm it was found and recognized.
    print(f'Found playlist: "{p.title}"')
    print(f'Started to download the audio from the playlist')
    for video in p.videos:
        try:
            # Print the title of the video currently being proccessed.
            print(f'Processing video: "{video.title}"')

            # filter the available streams for only audio streams.
            audio_stream = video.streams.filter(only_audio=True).first()
            # Check if an audio stream was successfully found
            if audio_stream:
                print(f'Downloading audio stream for "{video.title}"')
                # Downloading the selected audio stream.
                audio_stream.download(output_path=p.title)
                print(f'Succefully downloaded the stream audio"{video.title}"')
            else:
                # If no audio was found after filtered, print this message with failed and skip this video
                print(f'No available audio stream was found for "{video.title}". Skipping this video.')

        except Exception as e:
            #an error has occured from downloading video from the playlist
            #print the message and move to another song in the playlist
            print(f"an error has occured from downloading audio for \"{video.title}\": {e}", file=sys.stderr)
    
    # Print a message indicating that the processing of all videos in the place
    print("Finished processing all videos in the playlist.")

except Exception as e:
    #Print a critical error message and exit script.
    print(f"A critical error has occurred while trying to access the playlist: {e}", file=sys.stderr)
    sys.exit(1) #exit the script with a non-zero status code to indicate an error occured.