import '/imports/transactions/components/units';

startMovingUnit = (input) => executeTransaction({
  name: 'Start moving unit',
  steps: [
    checkIfAvailable,
    checkIfMoveAllowed,
    highlightPossibilities,
    saveOldCoordinates,
  ],
  input: input,
  failure: sendUnitBack
});
