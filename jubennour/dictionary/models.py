from django.db import models

# Multilingual dictionary based on Lexical Markup Framework (LMF)

class Lexicon(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LexicalEntry(models.Model):
    # parts-of-speech
    NOUN = 'noun'
    PNOUN = 'proper noun'
    VERB = 'verb'
    ADJECTIVE = 'adjective'
    ADVERB = 'adverb'
    CONJUNCTION = 'conjunction'
    PREPOSITION = 'preposition'
    PRONOUN = 'pronoun'
    INTERJECTION = 'interjection'
    NUMERAL = 'numeral'
    PARTICLE = 'particle'
    OTHER = 'other'
    POS_CHOICES = (
        (NOUN, _('noun')),
        (PNOUN, _('proper noun')),
        (VERB, _('verb')),
        (ADJECTIVE, _('adjective')),
        (ADVERB, _('adverb')),
        (CONJUNCTION, _('conjunction')),
        (PREPOSITION, _('preposition')),
        (PRONOUN, _('pronoun')),
        (INTERJECTION, _('interjection')),
        (NUMERAL, _('numeral')),
        (PARTICLE, _('particle')),
        (OTHER, _('other')),
    )

    lexicon = models.ForeignKey(Lexicon, on_delete=models.CASCADE)
    lemma = models.CharField(max_length=100)
    pos = models.CharField(max_length=100, choices=POS_CHOICES)



class Sense(models.Model):
    lexical_entry = models.ForeignKey(LexicalEntry, on_delete=models.CASCADE)
    sense_number = models.IntegerField()

class Form(models.Model):
    lexical_entry = models.ForeignKey(LexicalEntry, on_delete=models.CASCADE)
    phonetic_form = models.CharField(max_length=100)
    
    class Meta:
        abstract = True


class Lemma(Form):


class WordForm(Form):
    grammatical_number = models.CharField(max_length=100)
    grammatical_gender = models.CharField(max_length=100)
    grammatical_tense
    person

class FormRepresentation(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    written_form = models.CharField(max_length=100)
    orthography_name = models.CharField(max_length=100)