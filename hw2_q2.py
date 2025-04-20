from collections import namedtuple
from enum import Enum
from itertools import zip_longest

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def process_meeting(agent1, agent2):
    """Process the meeting of two agents and return their updated states."""
    if agent1.category == Condition.CURE:
        if agent2.category == Condition.SICK:
            agent2 = agent2._replace(category=Condition.HEALTHY)
        elif agent2.category == Condition.DYING:
            agent2 = agent2._replace(category=Condition.SICK)
    elif agent2.category == Condition.CURE:
        if agent1.category == Condition.SICK:
            agent1 = agent1._replace(category=Condition.HEALTHY)
        elif agent1.category == Condition.DYING:
            agent1 = agent1._replace(category=Condition.SICK)
    elif agent1.category == Condition.SICK and agent2.category == Condition.SICK:
        # Both agents worsen to DYING
        agent1 = agent1._replace(category=Condition.DYING)
        agent2 = agent2._replace(category=Condition.DYING)
    elif agent1.category == Condition.SICK and agent2.category == Condition.DYING:
        agent1 = agent1._replace(category=Condition.DYING)
        agent2 = agent2._replace(category=Condition.DEAD)
    elif agent1.category == Condition.DYING and agent2.category == Condition.SICK:
        agent1 = agent1._replace(category=Condition.DEAD)
        agent2 = agent2._replace(category=Condition.DYING)
    elif agent1.category == Condition.DYING and agent2.category == Condition.DYING:
        agent1 = agent1._replace(category=Condition.DEAD)
        agent2 = agent2._replace(category=Condition.DEAD)
    return agent1, agent2


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents."""
    # Separate agents into those who participate in meetings and those who don't
    meeting_agents = [agent for agent in agent_listing if agent.category not in {Condition.HEALTHY, Condition.DEAD}]
    non_meeting_agents = [agent for agent in agent_listing if agent.category in {Condition.HEALTHY, Condition.DEAD}]

    # Pair agents and process their meetings
    updated_agents = []
    for agent1, agent2 in zip_longest(meeting_agents[::2], meeting_agents[1::2], fillvalue=None):
        if agent2 is None:  # If there's an uneven number of agents
            updated_agents.append(agent1)
        else:
            updated_agent1, updated_agent2 = process_meeting(agent1, agent2)
            updated_agents.extend([updated_agent1, updated_agent2])

    # Combine updated meeting agents with non-meeting agents
    return updated_agents + non_meeting_agents


if __name__ == '__main__':
    # Example input for testing
    agents = (
        Agent("Adam", Condition.SICK),
        Agent("Cure0", Condition.CURE),
        Agent("Cure1", Condition.CURE),
        Agent("Bob", Condition.HEALTHY),
        Agent("Alice", Condition.DEAD),
        Agent("Charlie", Condition.DYING),
        Agent("Vaccine", Condition.SICK),
        Agent("Darlene", Condition.DYING),
        Agent("Emma", Condition.SICK),
        Agent("Cure2", Condition.CURE),
    )
    result = meetup(agents)
    print("Updated agents after meetings:")
    for agent in result:
        print(agent)
