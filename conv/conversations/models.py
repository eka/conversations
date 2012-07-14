from django.db import models

# Create your models here.


class Conversation(models.Model):
    title = models.CharField(max_length=25)
    users = models.ManyToManyField('auth.User')
    messages = models.ManyToManyField('conversations.Message', blank=True)

    class Meta:
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'

    def __unicode__(self):
        return u'%s - [%s] - messages: %s' % (self.title, ', '.join(map(str, self.users.all())), self.messages.count())
        # return u'%s' % self.title

    def last_message(self):
        return self.messages.latest('id')

class Message(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.TextField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __unicode__(self):
        return u'%s - %s' % (self.user, self.text)
