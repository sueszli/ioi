SELECT
    username,
    email,
    COUNT(items.id) as items,
    SUM(items.weight) as total_weight
FROM accounts
JOIN accounts_items ON accounts.id = accounts_items.account_id /* accounts_items is a join table */
JOIN items ON items.id = accounts_items.item_id
GROUP BY username, email
HAVING SUM(items.weight) > 20
ORDER BY total_weight DESC, username ASC
;