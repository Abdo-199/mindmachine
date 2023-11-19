
import nltk
from sentence_transformers import SentenceTransformer, util
import numpy as np
from LexRank import degree_centrality_scores

#nltk.download('punkt')

model = SentenceTransformer('all-MiniLM-L6-v2')

# Our input document we want to summarize
# As example, we take the first section from Wikipedia
document = """
Darth Revan, eine der faszinierendsten Figuren im Star Wars-Universum, ist eine zentrale Figur in der 
Ära der Alten Republik und in der Handlung vieler Star Wars-Videospiele und Romane. Seine Geschichte ist geprägt von einer tiefgreifenden Wandlung von einem gefeierten Jedi-Ritter zu einem mächtigen Sith-Lord und später zu einem Helden, der seine dunkle Vergangenheit überwindet, um erneut das Gute zu verteidigen. 
 
Die Geschichte von Darth Revan beginnt in den Zeiten der Alten Republik, einer Ära des Friedens und des Wohlstands, in der die Jedi-Ritter als Hüter des Friedens und der Gerechtigkeit bekannt sind. Revan, ursprünglich als ein hervorragender Jedi bekannt, war eine talentierte und charismatische Figur, die für seine Weisheit und seine Fähigkeiten in der Macht bewundert wurde. Gemeinsam mit seinem treuen Freund Malak führte er die Republik im Krieg gegen die Sith und galt als ein leuchtendes Vorbild für den Jedi-Orden. 
 
Jedoch änderte sich Revans Schicksal drastisch, als er während eines Konflikts mit den Sith-Lords auf die Dunkle Seite der Macht verführt wurde. Unter dem Einfluss der Dunklen Seite übernahm er den Namen Darth Revan und gründete ein mächtiges Sith-Imperium, das die Galaxis zu unterwerfen suchte. Unter Revans Führung begannen die Sith einen verheerenden Krieg gegen die Republik, der zu Chaos und Zerstörung führte und zahllose Welten in seinen Bann zog. 
 
Trotz seiner dunklen Taten erwies sich Revan als eine ambivalente Figur, die sowohl Macht als auch Mitgefühl besaß. In einem entscheidenden Moment kehrte Revan zur hellen Seite der Macht zurück, als er erkannte, dass die Sith-Prinzipien von Unterdrückung und Gewalt nicht der rechten Weg waren. Er brach mit dem Sith-Imperium und kämpfte nun auf Seiten der Republik, um seine Fehler wieder gut zu machen und den Frieden wiederherzustellen. 
 
Revan begab sich auf eine persönliche Quest, um seine Vergangenheit zu ergründen und sich mit seinen früheren Taten auseinanderzusetzen. Mit der Hilfe treuer Gefährten suchte er nach Erkenntnis und Wahrheit, um seine Verfehlungen zu sühnen. Sein Weg führte ihn zu verschiedenen Orten in der Galaxis, wo er sich gefährlichen Herausforderungen und Feinden stellen musste, die versuchten, ihn von seinem Weg abzubringen. 
 
Seine Reise brachte ihm nicht nur die Anerkennung vieler in der Republik, sondern auch die 
Vergebung einiger ehemaliger Feinde. Durch seine Taten wurde Revan zu einer Legende, deren 
Geschichte über die Jahrhunderte weitererzählt wurde. Seine Entscheidungen und Opfer dienten als Inspiration für viele nachfolgende Generationen von Jedi-Rittern, die seine Lehren und Prinzipien in Ehren hielten und weitertrugen. 
 
Die Geschichte von Darth Revan ist eine bewegende Saga von Macht, Verführung, Opfer und Erlösung, die den Kern der komplexen Natur des Star Wars-Universums verkörpert. Sein Erbe lebt in den Legenden und Geschichten der Galaxis fort und dient als zeitloses Beispiel für die ewige Konfrontation zwischen Licht und Dunkelheit. 
"""

#Split the document into sentences
sentences = nltk.sent_tokenize(document)
print("Num sentences:", len(sentences))

#Compute the sentence embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

#Compute the pair-wise cosine similarities
cos_scores = util.cos_sim(embeddings, embeddings).numpy()

#Compute the centrality for each sentence
centrality_scores = degree_centrality_scores(cos_scores, threshold=None)

#We argsort so that the first element is the sentence with the highest score
most_central_sentence_indices = np.argsort(-centrality_scores)


#Print the 5 sentences with the highest scores
print("\n\nSummary:")
for idx in most_central_sentence_indices[0:5]:
    print(sentences[idx].strip())