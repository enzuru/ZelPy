checkIfAvailable = (input) => {
  if (input.unit.status != 'available') {
    return new Left('Unit is not available');
  }

  return new Right(input);
}
