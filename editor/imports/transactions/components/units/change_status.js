changeStatus = (input) => {
  input.unit.status = 'moved';

  return new Right(input);
}
