executeTransaction = (args) => {
  const name = args.name;
  const steps = args.steps;
  const failure = args.failure;

  var input = args.input;
  var result;

  console.log(name);
  for (let step of steps) {
    result = step(input);
    console.log(step.name);
    if (result instanceof Left) {
      console.log('Failure: ' + result.error);
      failure(input);
      break;
    }
    input = result.value;
  }
  
  return new Right(input);
}
