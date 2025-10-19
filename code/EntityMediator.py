import pygame

from code import player
from code.enemyForward import EnemyForward
from code.enemyReverse import EnemyReverse
from code.entity import Entity
from code.player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): #faz as entidades sumirem após ultrapassarem a margem esquerda
        if isinstance(ent, EnemyForward):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, EnemyReverse):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
               entity_list.remove(ent)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, EnemyForward):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyReverse):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                now = pygame.time.get_ticks()
                INVULN_MS = 800

                if now > getattr(player, "invulnerable_until", 0):
                    ent1.health -= ent2.damage
                    player.invulnerable_until = now + INVULN_MS
                    if getattr(ent1, "collision_sound", None) is not None:
                        ch = pygame.mixer.find_channel()
                        if ch is not None:
                            ch.play(ent1.collision_sound)
                        else:
                            ent1.collision_sound.play()
                else:
                    pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)


