checkIfMoveAllowed = (input) => {
  if (input.unit.player != input.unit.client.player) {
    return new Left("Unit does not belong to player");
  }
  return new Right(input);
}
