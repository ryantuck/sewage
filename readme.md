# Sewage

An experiment in simple, python-only data transformations.

Sewage consists of two concepts: models and transforms.

Models are implemented as `pydantic` models, giving the operator complete control over schema enforcement, and coupling code to documentation.

Transforms are pure functions that accept input models and produce output models.

Sewage is primarily concerned about Extracting and Transforming data, and treats Loading data as an implementation detail. Models can conditionally persist to a local data store, DynamoDB, S3, etc.

## TBD

It seems like type hints should be the sole place where valid transforms are defined. It would be nice to be able to access that info as a data structure, allowing the operator to call `downstream_model()` and pass in any valid model that it can read from, and automatically invoking the only valid function that could handle converting the input into the expected output. In the meantime, I'm essentially falling back on a `switch` statement across valid input types. One naive way to handle this is to bang through all possible functions for converting the thing and ignoring specific typing-related errors. Using try/catch for flow control smells bad, but it's doable.





