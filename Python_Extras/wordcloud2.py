from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = input('Enter your string : ')

cloud = WordCloud(background_color="white").generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()
