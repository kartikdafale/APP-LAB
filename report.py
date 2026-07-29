# Define the Report class
class Report:
    # Class variable for storing templates
    templates = {}

    # Constructor to initialize the report with title and content
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add a template to the class variable
    @classmethod
    def add_template(cls, name, template_func):
        cls.templates[name] = template_func

    # Class method to retrieve a template from the class variable
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method to call a report instance with a template name
    def __call__(self, template_name):
        template = self.get_template(template_name)
        if template:
            return template(self)
        else:
            return "Template not found."

    # String representation of the report
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"


# Define a simple template function
def simple_template(report):
    return f"Simple Report\nTitle: {report.title}\nContent: {report.content}"


# Define a fancy template function with bold formatting
def fancy_template(report):
    return (
        f"*** {report.title.upper()} ***\n"
        f"**{report.content}**"
    )


# Main function to generate and display reports
def main():
    # Add templates to the Report class
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create a report instance
    report = Report("Monthly Sales", "Sales increased by 20% this month.")

    # Generate reports with different templates
    simple_report = report("simple")
    fancy_report = report("fancy")

    # Display the reports
    print("Default Report:")
    print(report)

    print("\nSimple Template:")
    print(simple_report)

    print("\nFancy Template:")
    print(fancy_report)


# Run the main function
if __name__ == "__main__":
    main()