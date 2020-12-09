from django.db import models
from ..base import BaseModel


class User(BaseModel):
    user_id = models.BigIntegerField(primary_key=True)
    is_deleted = models.BooleanField(null=True, blank=True)
    is_bot = models.BooleanField(null=True, blank=True)
    is_verified = models.BooleanField(null=True, blank=True)
    is_restricted = models.BooleanField(null=True, blank=True)
    is_scam = models.BooleanField(null=True, blank=True)
    is_support = models.BooleanField(null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    language_code = models.CharField(max_length=20, null=True, blank=True)
    dc_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    ##############################################################
    deleted_at = models.BigIntegerField(null=True, blank=True)

    # `telegram_accounts` : telegram accounts connected to this user
    # `restrictions` : restrictions of this user if it's a bot
    # `admin_log_mentions` : admin logs this user is mentioned in
    # `admin_log_events` : admin logs this user has committed
    # `forwarded_messages` : forwarded messages from this user
    # `messages` : messages belonging to this user in a chat
    # `via_bot_messages` : messages (inline queries) that were generated by this bot in a chat
    # `mentioned_entities` : entities that this user is mentioned in
    # `chats` : chats this users is/was member of (including state; is current member or left the chat)
    # `promoted_participants` : channel participants promoted by this user
    # `demoted_participants` : channel participants demoted by this user
    # `invited_participants` : channel participants invited by this user
    # `kicked_participants` : channel participants kicked by this user

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        # return str(self.first_name if self.first_name else "") + str(self.last_name if self.last_name else "")
        return f"{self.first_name if self.first_name else self.last_name if self.last_name else ''} `@{self.username if self.username else self.user_id}`"
