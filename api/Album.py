from mutagen.id3 import ID3, APIC

audio = ID3('Zinoleesky-Joromi-NAIJABEAT.COM.mp3')

with open('naijabeat.jpeg', 'rb') as albumart:
    audio['APIC'] = APIC(
                      encoding=3,
                      mime='image/jpeg',
                      type=3, desc=u'Cover',
                      data=albumart.read()
                    )

audio.save()