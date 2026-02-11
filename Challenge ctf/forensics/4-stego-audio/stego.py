import wave

def hide_message(input_wav, output_wav, message):
    audio = wave.open(input_wav, 'rb')
    params = audio.getparams()
    frames = audio.readframes(audio.getnframes())
    audio.close()

    # Convert message to bits
    bits = ''.join(format(ord(c), '08b') for c in message)
    bits += '00000000' # Null terminator

    frames = bytearray(frames)
    for i in range(len(bits)):
        frames[i] = (frames[i] & 0xFE) | int(bits[i])

    new_audio = wave.open(output_wav, 'wb')
    new_audio.setparams(params)
    new_audio.writeframes(frames)
    new_audio.close()

# Example usage (not run here):
# hide_message('carrier.wav', 'secret.wav', 'CTF{lsb_4ud10_st3g0_1s_tr1cky}')
