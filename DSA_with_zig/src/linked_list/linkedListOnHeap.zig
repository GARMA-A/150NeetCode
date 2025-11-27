const std = @import("std");
const testing = std.testing;

pub fn LinkList(comptime T: type) type {
    return struct {
        const Node = struct {
            next: ?*Node = null,
            prev: ?*Node = null,
            data: T,
        };
        const Self = @This();
        head: ?*Node,
        tail: ?*Node,
        len: usize,
        alloc: std.mem.Allocator,

        pub fn init(allocator: std.mem.Allocator) Self {
            return Self{ .len = 0, .alloc = allocator, .head = null, .tail = null };
        }
        pub fn deinit(self: *Self) void {
            while (self.pop()) |_| {}
        }

        pub fn push(self: *Self, val: T) !void {
            const newNode = try self.alloc.create(Node);
            newNode.data = val;
            newNode.next = null;
            newNode.prev = self.tail;
            if (self.tail) |node| {
                node.next = newNode;
            } else {
                self.head = newNode;
            }
            self.len += 1;
            self.tail = newNode;
        }

        pub fn pop(self: *Self) ?T {
            const node = self.tail orelse return null;
            defer self.alloc.destroy(node);
            self.tail = node.prev;
            self.len -= 1;
            return node.data;
        }

        pub fn display(self: *Self) void {
            var cur = self.head;
            while (cur) |node| : (cur = node.next) {
                std.debug.print("{any} ,", .{node.data});
            }

            std.debug.print("\n", .{});
        }
    };
}

test "the push pop methods" {
    var my_Linked_List = LinkList(i32).init(testing.allocator);
    defer my_Linked_List.deinit();

    try my_Linked_List.push(12);
    try my_Linked_List.push(13);

    try testing.expect(my_Linked_List.pop() == 13);

    try testing.expect(my_Linked_List.pop() == 12);

    try testing.expect(my_Linked_List.pop() == null);

    try my_Linked_List.push(100);

    try testing.expect(my_Linked_List.pop() == 100);
}

test "push pop methods track the len properity" {
    var my_Linked_List = LinkList(i32).init(testing.allocator);
    defer my_Linked_List.deinit();

    try my_Linked_List.push(12);
    try my_Linked_List.push(13);
    try testing.expectEqual(2, my_Linked_List.len);
    try my_Linked_List.push(14);
    try my_Linked_List.push(15);
    try testing.expectEqual(4, my_Linked_List.len);
    _ = my_Linked_List.pop();
    _ = my_Linked_List.pop();
    try testing.expectEqual(2, my_Linked_List.len);
}

test "the display method" {
    var my_Linked_List = LinkList(i32).init(testing.allocator);
    defer my_Linked_List.deinit();

    try my_Linked_List.push(1);
    try my_Linked_List.push(2);
    try my_Linked_List.push(3);
    try my_Linked_List.push(4);
    try my_Linked_List.push(5);

    my_Linked_List.display(); // Expected output: 1 ,2 ,3 ,4 ,5 , // confirmed

}
