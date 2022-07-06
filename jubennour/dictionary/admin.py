from django.contrib import admin

from .models import Form, LexicalEntry, Lemma, Sense, WordForm, Lexicon, SenseAxis, ListOfComponents, Component, FormRepresentation

class SenseInline(admin.TabularInline):
    model = Sense
    extra = 0

class LexicalEntryAdmin(admin.ModelAdmin):
    inlines = [SenseInline]
    list_display = ('lemma', 'pos')
    list_filter = ('lexicon', 'pos')
    search_fields = ('lexicon', 'pos', 'lemma')


admin.site.register(Lexicon)
admin.site.register(FormRepresentation)
admin.site.register(Lemma)
admin.site.register(SenseAxis)
admin.site.register(LexicalEntry, LexicalEntryAdmin)