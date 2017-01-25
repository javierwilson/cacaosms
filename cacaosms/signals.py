from django.db.models.signals import post_save
from django.dispatch import receiver

from cacaosms.taskapp.celery import send_sms
from cacaosms.models import Envios, Contacto


@receiver(post_save, sender=Envios, dispatch_uid="send_sms_to_queue")
def send_sms_to_queue(sender, instance, **kwargs):

    task = None

    if instance.para_contacto:
        contact = instance.para_contacto
        print "%s: %s" % (contact.full_number, instance.message)
        print send_sms.name
        task = send_sms.delay(contact.full_number, instance.message)

    if instance.para_pais:
        contacts = Contacto.objects.filter(pais=instance.para_pais)
        for contact in contacts:
            print "%s: %s" % (contact.full_number, instance.message)
            task = send_sms.delay(contact.full_number, instance.message)

    if instance.para_grupo:
        contacts = Contacto.objects.filter(grupo=instance.para_grupo)
        for contact in contacts:
            print "%s: %s" % (contact.full_number, instance.message)
            task = send_sms.delay(contact.full_number, instance.message)

    if task:
        print task.status
