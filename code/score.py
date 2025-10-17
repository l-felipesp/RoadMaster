import pygame

from code import player


class ScoreSystem:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.score = 0

    def reset(self):
        """Reseta o sistema de pontuação (chamado quando o jogo reinicia)."""
        self.start_time = pygame.time.get_ticks()
        self.score = 0

    def update(self, player_lane):
        """
        Atualiza a pontuação com base no tempo de sobrevivência e na faixa atual do jogador.

        player_lane: int (0 a 3) — posição do jogador na pista.
        """
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000  # segundos

        # Calcula multiplicador com base na faixa
        # Faixa 0 (esquerda, mão) → 1x
        # Faixa 1 → 1.2x
        # Faixa 2 (contramão) → 1.5x
        # Faixa 3 (contramão e beirada) → 2x
        lane_multipliers = [1.0, 1.2, 1.5, 2.0]
        multiplier = lane_multipliers[player_lane]

        # Pontuação é tempo vivo * multiplicador da faixa atual
        # (Você pode acumular ou apenas mostrar esse valor)
        player.score = elapsed_time * multiplier

    def get_score(self):
        return int(self.score)
