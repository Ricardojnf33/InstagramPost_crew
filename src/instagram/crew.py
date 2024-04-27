from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from instagram.tools.search import SearchTools


# Uncomment the following line to use an example of a custom tool
# from instagram.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class InstagramCrew():
	"""Instagram crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			tool=[
				SearchTools.search_internet,
				SearchTools.search_instagram,
				SearchTools.open_page,
			],
			verbose=True,
		)

	
	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['content_strategist'],
			verbose=True,
		)
	
	
	@agent
	def visual_describer(self) -> Agent:
		return Agent(
			config=self.agents_config['visual_describer'],
			verbose=True,
			allow_delegation=False,
		)
	
	
	@agent
	def copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config['copywriter'],
			verbose=True,
		)

	
	@task
	def market_research(self) -> Task:
		return Task(
			config=self.tasks_config['market_research'],
			agent=self.market_researcher(),
			output_file="relatórios/market_research.md",
		)

	@task
	def content_strategy_development(self) -> Task:
		return Task(
			config=self.tasks_config['content_strategy_development'],
			agent=self.content_strategist(),
		)

	@task
	def visual_content_creation(self) -> Task:
		return Task(
			config=self.tasks_config['visual_content_creation'],
			agent=self.visual_describer(),
			output_file="relatórios/visual_description.md"
		)
	
	@task
	def copywriting(self) -> Task:
		return Task(
			config=self.tasks_config['copywriting'],
			agent=self.copywriter(),
			output_file="relatórios/copy_post.md"
		)
	
	@task
	def report_final_content_strategy(self) -> Task:
		return Task(
			config=self.tasks_config['report_final_content_strategy'],
			agent=self.content_strategist(),
			output_file="relatórios/final-content-strategy.md"
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Instagram crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)