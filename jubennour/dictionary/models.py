from django.utils.translation import gettext as _
from django.db import models

# Multilingual dictionary based on Lexical Markup Framework (LMF)


class Lexicon(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FormRepresentation(models.Model):
    written_form = models.CharField(max_length=100)
    orthography_name = models.CharField(max_length=100, blank=True)


class Form(models.Model):
    phonetic_form = models.CharField(max_length=100, blank=True)
    form_representation = models.OneToOneField(
        FormRepresentation, on_delete=models.RESTRICT)


class Lemma(Form):

    def __str__(self):
        return self.form_representation.written_form


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
    POS_CHOICES = (  # (value, display-name)
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
    pos = models.CharField(max_length=100, choices=POS_CHOICES)
    lemma = models.OneToOneField(Lemma, on_delete=models.RESTRICT)

    def __str__(self):
        return self.lemma.form_representation.written_form


class WordForm(Form):
    lexical_entry = models.ForeignKey(LexicalEntry, on_delete=models.CASCADE)

    # grammatical numbers
    SINGULAR = 'singular'
    PLURAL = 'plural'
    DUAL = 'dual'
    COLLECTIVE = 'collective'
    NUMBER_CHOICES = (  # (value, display-name)
        (SINGULAR, _('singular')),
        (PLURAL, _('plural')),
        (DUAL, _('dual')),
        (COLLECTIVE, _('collective')),
    )

    # persons
    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    PERSON_CHOICES = (  # (value, display-name)
        (FIRST, _('first')),
        (SECOND, _('second')),
        (THIRD, _('third')),
    )

    # grammatical genders
    MASCULINE = 'masculine'
    FEMININE = 'feminine'
    NEUTRAL = 'neutral'
    GENDER_CHOICES = (
        (MASCULINE, _('masculine')),
        (FEMININE, _('feminine')),
        (NEUTRAL, _('neutral')),
    )

    # grammatical tenses
    PRESENT = 'present'
    IMPERFECT = 'imperfect'
    PAST = 'past'
    FUTURE = 'future'
    TENSE_CHOICES = (
        (PRESENT, _('present')),
        (IMPERFECT, _('imperfect')),
        (PAST, _('past')),
        (FUTURE, _('future')),
    )

    # grammatical moods
    INDICATIVE = 'indicative'
    CONJUNCTIVE = 'conjunctive'
    CONDITIONAL = 'conditional'
    PARTICIPLE = 'participle'
    SUBJUNCTIVE = 'subjunctive'
    IMPERATIVE = 'imperative'
    INFINITIVE = 'infinitive'
    MOOD_CHOICES = (
        (INDICATIVE, _('indicative')),
        (CONJUNCTIVE, _('conjunctive')),
        (CONDITIONAL, _('conditional')),
        (PARTICIPLE, _('participle')),
        (SUBJUNCTIVE, _('subjunctive')),
        (IMPERATIVE, _('imperative')),
        (INFINITIVE, _('infinitive')),
    )

    grammatical_number = models.CharField(
        max_length=25, choices=NUMBER_CHOICES, blank=True)
    grammatical_gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, blank=True)
    grammatical_tense = models.CharField(
        max_length=25, choices=TENSE_CHOICES, blank=True)
    grammatical_mood = models.CharField(
        max_length=25, choices=MOOD_CHOICES, blank=True)
    person = models.CharField(
        max_length=25, choices=PERSON_CHOICES, blank=True)

    def __str__(self):
        return self.form_representation.written_form


class ListOfComponents(models.Model):
    lexical_entry = models.ForeignKey(LexicalEntry, on_delete=models.CASCADE)


class Component(models.Model):
    list_of_components = models.ForeignKey(
        ListOfComponents, on_delete=models.CASCADE)
    lexical_entry = models.ForeignKey(LexicalEntry, on_delete=models.CASCADE)
    component_number = models.IntegerField()

    def __str__(self):
        return self.lexical_entry.lemma.form_representation.written_form


class SenseAxis(models.Model):
    source = models.CharField(max_length=100, blank=True)



class Sense(models.Model):
    definition = models.TextField(blank=True)
    lexical_entry = models.ForeignKey(LexicalEntry, on_delete=models.CASCADE)
    sense_number = models.IntegerField()
    sense_axiss = models.ManyToManyField(SenseAxis, blank=True)

    def __str__(self):
        return self.lexical_entry.lemma.form_representation.written_form + str(self.sense_number)
