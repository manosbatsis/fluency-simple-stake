pragma solidity ^0.8.0;

import "./CustomToken.sol";

/**
 * @dev Extension of {ERC20} that adds staking mechanism.
 */
contract TestableCustomToken is CustomToken {

    // Make _stake testable
    function stake(address sender, uint256 amount) public {
        _stake(sender, amount);
    }

    // Make _unstake testable
    function unstake(address sender) public {
        _unstake(sender);
    }

}