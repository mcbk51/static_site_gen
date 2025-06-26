
def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    block_list = []
    for block in blocks:
        if block == "":
            continue
        bloc = block.strip()
        block_list.append(block)
    return block_list
