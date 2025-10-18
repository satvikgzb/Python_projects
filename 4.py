import time
import random
import keyboard

paragraphs = ['The sun peeked through the early morning clouds, casting golden rays across the sleepy village. Birds chirped from tree branches, adding life to the quiet surroundings. A gentle breeze rustled the leaves as the day slowly awakened. Children prepared for school, while farmers readied their tools for the fields. Smoke curled from chimneys, carrying the scent of breakfast. The peaceful rhythm of village life followed nature’s lead. There was no rush, only the steady pulse of a new beginning. Each day, the same pattern unfolded, comforting in its familiarity. This was life here: simple, slow, and quietly beautiful in every way.'

'Technology has transformed the way we communicate, work, and learn. From smartphones to high-speed internet, digital tools are now a part of our daily routines. Remote work and online learning have become common, offering flexibility and access like never before. However, this digital shift comes with its challenges—screen fatigue, decreased face-to-face interaction, and concerns about privacy. Balancing these benefits and drawbacks is essential as we continue to integrate technology into more areas of life. As the pace of innovation accelerates, adaptability becomes a valuable skill. Those who can learn, unlearn, and relearn quickly will thrive in this evolving digital world.'

'The forest was dense, filled with the sounds of rustling leaves and distant calls of wildlife. Sunlight barely touched the ground, blocked by a thick canopy above. Moss-covered logs lined the trail, and the scent of earth and pine lingered in the air. Every step forward felt like a journey deeper into an ancient world untouched by time. Birds fluttered overhead, while small creatures darted through underbrush. The deeper one ventured, the quieter it became, the forest absorbing all sound. It was easy to feel both lost and completely free here. Nature surrounded you, reminding you how small you really are.'

'In a world of constant noise and endless distractions, finding moments of silence has become increasingly rare. Yet silence is essential—it allows the mind to rest, reset, and reflect. Without it, creativity suffers and stress grows. Taking time each day for quiet contemplation can improve mental clarity and emotional balance. Whether it’s a walk without your phone, sitting in a quiet room, or simply closing your eyes for a minute, silence is a powerful tool. In stillness, we often find answers we didn’t know we were looking for. Embrace silence not as absence, but as presence in its most mindful form.'

'Traveling introduces us to new cultures, ideas, and perspectives. Each destination holds its own charm, shaped by history, geography, and people. Whether wandering ancient streets, tasting unfamiliar foods, or hearing new languages, travel stretches our understanding of the world. It challenges assumptions, builds empathy, and often leaves lasting memories. Even small trips offer the chance to step outside routine and rediscover wonder. The best journeys aren’t always about distance—they’re about depth of experience. While photos capture moments, it’s the emotions and connections that linger. In the end, travel teaches us more about others—and ourselves—than we ever expect at the beginning.']


para= random.choice(paragraphs)

print('Type the following paragraph/n')
print('para')
print('Start typing and press ENTER when done')

typed_text = ''
start_time = None

def on_key(event):
    global start_time,typed_text
    if start_time is None:
        start_time = time.time()
    if event.name == 'enter':
        keyboard.unhook_all()
    else:
        typed_text += event.name if len(event.name) == 1 else ''


keyboard.on_press(on_key)
keyboard.wait("enter")

end_time = time.time()
time_taken = end_time - start_time
time_min = time_taken/60
time_sec = time_taken%60
total_words= len(para)


word_count = len(typed_text.split())
wpm = word_count/time_min

original_words = para.split()
typed_words = typed_text.split()


correct_words = 0
for orig,typed in zip(original_words,typed_words):
    if orig == typed:
        correct_words += 1
accuracy = (correct_words/total_words)*100

print(f'You typed {total_words} words in {time_min} minutes and {time_sec} seconds!')
print(f'Your typing speed was {wpm} with the accuracy of {accuracy}% !')





