import '/imports/transactions/components/units';

endMovingUnit = (input) => executeTransaction({
  name: 'End moving unit',
  steps: [
    removeHighlights,
    checkIfDistanceAllowed,
    saveMove,
    //changeStatus,
    //popupOptions,
  ],
  input: input,
  failure: sendUnitBack
});
