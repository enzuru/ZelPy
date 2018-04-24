import '/imports/transactions/components/units'

updateMovingUnit = (input) => executeTransaction({
  name: 'Update moving unit',
  steps: [
    flipUnitDirection,
  ],
  input: input,
  failure: sendUnitBack
})
