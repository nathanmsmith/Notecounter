import midi, sys

if len(sys.argv) != 2:
    print "Usage: {0} <midifile>".format(sys.argv[0])
    sys.exit(2)

midifile = sys.argv[1]
pattern = midi.read_midifile(midifile)

total = 0
notecount = [['c', 0], ['c#', 0], ['d', 0], ['d#', 0], ['e', 0], ['f', 0], ['f#', 0], ['g', 0], ['g#', 0], ['a', 0], ['a#', 0], ['b', 0]] #array of total of each types of notes

for track in pattern:
    for event in track:
        if type(event) is midi.events.NoteOnEvent:
            for i in range(0, 12):
                if event.data[0] in range(i, 120+i, 12):  #data[0] is pitch, [1] is velocity
                    notecount[i][1] += 1
            total +=1
            
print "File:", midifile
print "Number of notes:", total
print "Breakdown:"
for i in range(0, 12):
    print notecount[i][0] + ":", notecount[i][1]
