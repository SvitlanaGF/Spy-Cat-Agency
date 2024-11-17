# Spy Cat Agency

## Models:
### SpyCat:
 - Name;
- yearsOfExperience;
 - breed;
 - salary(can change).
### Missions:
- Cat
- Targets
- Complete state

### Target:
- Name
- Country
- Notes
- Complete state


# Main Tasks:
- **Spy Cats**
    - Ability to create a spy cat in the system
        - A cat is described as Name, Years of Experience, Breed, and Salary. +
        - Breed must be validated, see General
    - Ability to remove spy cats from the system
    - Ability to update spy cats’ information (Salary)
    - Ability to list spy cats +
    - Ability to get a single spy cat
- **Missions / Targets**
    - Ability to create a mission in the system along with targets in one single request
        - A mission contains information about Cat, Targets and Complete state
        - Each target is unique to a mission, so the endpoint should accept an object describing targets
        - A target is described as Name, Country, Notes and Complete state
    - Ability to delete a mission
        - A mission cannot be deleted if it is already assigned to a cat
    - Ability to update mission targets
        - Ability to mark it as completed
        - Ability to update Notes
            - Notes cannot be updated if either the target or the mission is completed
    - Ability to assign a cat to a mission
    - Ability to list missions
    - Ability to get a single mission
- **General**
    - Framework
        - Use any of: FastAPI, Django
    - Database
        - You can use any database
    - Validations
        - Make sure endpoints validate the request body and return an adequate status code if it’s not valid

### Sharing the results

- Make a repository on Github
- Add a README explaining how to build/start the application. Include any information you think will be useful for us
- Define all of the endpoints in a Postman collection and add link to it in the README
- As you have the repository in place, share a link to it with our recruiter. We will review it within 2-3 business days and return with a feedback
- Don't hesitate to ask any questions

Thank you!