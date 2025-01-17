from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import DirectoryReadTool, FileReadTool
from crewai.project import CrewBase, agent, crew, task
llm_google = LLM(model="gemini/gemini-1.5-pro",  temperature=0.7, convert_system_message_to_human=True)
llm_openai = LLM(model="gpt-4o-mini", temperature=0.7)
llm_local = LLM(model="ollama/mixtral:8x7b", base_url="http://localhost:11434")

# Instantiate tools
docs_tool = DirectoryReadTool(directory='/Users/mdsweatt/Documents/Pycharm_Projects/Code_Extractor_Crew/code_repository')
file_tool = FileReadTool()

@CrewBase
class CodeExtractorCrew():
	"""CodeExtractorCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def code_parser(self) -> Agent:
		return Agent(
			config=self.agents_config['code_parser'],
			verbose=True,
			tools=[docs_tool, file_tool],
			llm=llm_openai
		)

	@agent
	def control_flow_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['control_flow_analyzer'],
			verbose=True,
			tools=[docs_tool, file_tool],
			llm=llm_openai
		)

	@agent
	def data_flow_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['data_flow_analyzer'],
			verbose=True,
			tools=[docs_tool, file_tool],
			llm=llm_openai
		)

	@agent
	def requirement_synthesizer(self) -> Agent:
		return Agent(
			config=self.agents_config['requirement_synthesizer'],
			verbose=True,
			tools=[docs_tool, file_tool],
			llm=llm_openai
		)

	@agent
	def requirement_validator(self) -> Agent:
		return Agent(
			config=self.agents_config['requirement_validator'],
			verbose=True,
			tools=[docs_tool, file_tool],
			llm=llm_openai
		)

	@task
	def parse_code(self) -> Task:
		return Task(
			config=self.tasks_config['parse_code'],
		)

	@task
	def analyze_control_flow(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_control_flow'],
			output_file='report.md'
		)

	@task
	def analyze_data_flow(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_data_flow'],
		)

	@task
	def synthesize_requirements(self) -> Task:
		return Task(
			config=self.tasks_config['synthesize_requirements'],
			output_file='report.md'
		)

	@task
	def validate_requirements(self) -> Task:
		return Task(
			config=self.tasks_config['validate_requirements'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CodeExtractorCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
