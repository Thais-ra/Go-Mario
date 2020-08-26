import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Cria o ambiente
env = gym_super_mario_bros.make('SuperMarioBros-1-1-v1')

# Restringe nossas ações somente às de movimentação
env = JoypadSpace(env, SIMPLE_MOVEMENT)

def run_episode(env):
    # Reseta o ambiente
    state = env.reset()
    # Roda um loop que toma ações enquanto um episódio não é terminado
    done = False
    while not done:
        # Escolhe uma ação aleatória
        action = env.action_space.sample()
        
        # Toma a ação escolhida e recebe as informações do próximo estado
        state, reward, done, _ = env.step(action)
        
        # Renderiza o ambiente
        env.render()

    # Fecha o ambiente
    env.close()

    # Roda o ambiente
run_episode(env)