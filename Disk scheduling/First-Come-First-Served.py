def FCFS(requests,head):
    seek_count=0 ; current_track=head
    for track in requests:
        distance=abs(track-current_track)
        seek_count+=distance
        current_track=track
    return seek_count,current_track

if __name__== '__main__':
    requests=[82,170,43] ; head=50
    seek_count,current_track=FCFS(requests,head)
    print(seek_count,current_track)



