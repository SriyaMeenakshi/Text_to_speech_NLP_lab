import asyncio
import edge_tts


async def generate_speech(text, voice, rate, pitch, output_file):
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch
    )

    await communicate.save(output_file)


def generate(text, voice, rate, pitch, output_file):
    asyncio.run(
        generate_speech(
            text,
            voice,
            rate,
            pitch,
            output_file
        )
    )